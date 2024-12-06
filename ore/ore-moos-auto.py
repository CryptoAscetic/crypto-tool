import paramiko

print("          欢迎使用Ore-Moos脚本")
print("本工具通过Python对VPS进行SSH连接部署Ore挖矿环境")
print("   部署完毕后 自行SSH连接VPS 执行  ./run.sh")


def ssh_exec_commands(hostname, username, password, port=22):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)

        # 需要执行的命令列表
        commands = [
            "sudo apt update",
            "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs",
            "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y npm",
            "npm install pm2 -g",
            "curl https://sh.rustup.rs  -sSf | sh -s -- -y",
            '. "$HOME/.cargo/env"',
            'sh -c "$(curl -sSfL https://release.solana.com/v1.18.4/install)"',
            'export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH"',
            "cargo install ore-cli"
        ]

        # 遍历命令列表，依次执行
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command, get_pty=True)
            exit_status = stdout.channel.recv_exit_status()  # 等待命令执行完成

        stdin, stdout, stderr = client.exec_command("mkdir -p ~/ore")
        print(stdout.read().decode())

        num_wallets = int(input("请输入要创建的钱包数量: "))
        common_rpc = input("请输入RPC地址: ")

        # 创建钱包的逻辑
        for i in range(1, num_wallets + 1):
            wallet_commands = [
                "/root/.local/share/solana/install/releases/1.18.4/solana-release/bin/solana-keygen new --no-bip39-passphrase",
                f"mv ~/.config/solana/id.json ~/.config/solana/{i}.json"
            ]

            for wallet_command in wallet_commands:
                stdin, stdout, stderr = client.exec_command(wallet_command, get_pty=True)

            # 生成 ore 和 claim 脚本
            ore_script = f"""#!/bin/bash
ore --rpc {common_rpc} --keypair ~/.config/solana/{i}.json --priority-fee 30000000 mine --threads 4
"""
            claim_script = f"""#!/bin/bash
ore --rpc {common_rpc} --keypair ~/.config/solana/{i}.json claim
"""
            ore_file = f"~/ore/ore{i}.sh"
            claim_file = f"~/ore/claim{i}.sh"
            client.exec_command(f'echo "{ore_script}" > {ore_file} && chmod +x {ore_file}')
            client.exec_command(f'echo "{claim_script}" > {claim_file} && chmod +x {claim_file}')

        # 生成 cx.sh 脚本
        cx_script = rf"""#!/bin/bash
keypairs=(~/.config/solana/*.json)

for config in "${{keypairs[@]}}"
do
    ore --rpc {common_rpc} --keypair "$config" rewards
done
"""
        client.exec_command(f'echo "{cx_script}" > ~/ore/cx.sh && chmod +x ~/ore/cx.sh')

        # 生成 run.sh 脚本
        run_script = """
#!/bin/bash

# 默认脚本存放路径
default_directory="/root/ore"
# Solana配置文件路径
solana_config_path="/root/.config/solana/"

# 修改RPC函数
modify_rpc() {
    read -p "请输入新的RPC地址：" new_rpc
    echo "正在修改 $default_directory 下的所有脚本的RPC地址为 $new_rpc ..."

    # 遍历目录下的所有.sh文件
    for file in $default_directory/*.sh
    do
        # 检查文件是否存在并且可读写
        if [ -f "$file" ] && [ -w "$file" ]; then
            # 修改RPC地址
            sed -i "s|--rpc.*--keypair|--rpc $new_rpc --keypair|" "$file"
            echo "已成功修改 $file 的RPC地址为 $new_rpc"
        else
            echo "无法修改 $file，文件不存在或无法访问。"
        fi
    done
}

# 修改Gas费函数
modify_gas() {
    read -p "请输入新的Gas费值：" new_gas_fee
    echo "正在修改 $default_directory 下的所有脚本的Gas费值为 $new_gas_fee ..."

    # 遍历目录下的所有.sh文件
    for file in $default_directory/*.sh
    do
        # 检查文件是否存在并且可读写
        if [ -f "$file" ] && [ -w "$file" ]; then
            # 修改Gas费值
            sed -i "s|--priority-fee [0-9]* mine|--priority-fee $new_gas_fee mine|" "$file"
            echo "已成功修改 $file 的Gas费值为 $new_gas_fee"
        else
            echo "无法修改 $file，文件不存在或无法访问。"
        fi
    done
}

# 开始挖矿函数
start_mining() {
    echo "正在开始挖矿..."
    pm2 start ore*.sh
}

# 停止挖矿函数
stop_mining() {
    echo "正在停止挖矿..."
    pm2 stop ore*.sh
}

# 开始Claim函数
start_claim() {
    echo "正在开始Claim..."
    pm2 start claim*.sh
}

# 停止Claim函数
stop_claim() {
    echo "正在停止Claim..."
    pm2 stop claim*.sh
}

# 查询数量函数
query_amount() {
    echo "正在查询数量..."
    # 进入脚本所在路径并执行
    cd "$default_directory" || return
    ./cx.sh
    # 执行完毕后返回上级路径
    cd - || return
}

# 更新Ore-CiL函数
update_ore_cli() {
    echo "正在更新 Ore-CiL..."
    cargo install ore-cli
}

# 查看钱包私钥函数
view_wallet_private_key() {
    # 列出Solana配置文件夹中的所有.json文件
    json_files=("$solana_config_path"*.json)
    if [ ${#json_files[@]} -eq 0 ]; then
        echo "未找到任何JSON文件在 $solana_config_path"
        return
    fi

    echo "找到以下JSON文件："
    for ((i=0; i<${#json_files[@]}; i++)); do
        echo "$((i+1)). ${json_files[$i]}"
    done

    # 选择JSON文件
    read -p "请选择要查看的JSON文件编号：" json_choice
    if [[ $json_choice =~ ^[0-9]+$ ]] && [ $json_choice -ge 1 ] && [ $json_choice -le ${#json_files[@]} ]; then
        selected_json="${json_files[$((json_choice-1))]}"
        echo "您选择了 $selected_json"
        echo "文件内容如下："
        cat "$selected_json"
    else
        echo "无效的选择，请输入有效的编号。"
    fi
}

# 主菜单函数
main_menu() {
    echo "欢迎使用ORE-Moos交互式脚本！"
    echo "作者TG：https://t.me/TonMoos"
    echo "作者Twitter：https://twitter.com/Moos_ton"
    echo "请选择一个选项："
    echo "1. 修改RPC"
    echo "2. 修改Gas费"
    echo "3. 开始挖矿"
    echo "4. 停止挖矿"
    echo "5. 开始Claim"
    echo "6. 停止Claim"
    echo "7. 查询数量"
    echo "8. 更新Ore-CiL(部署后请先更新)"
    echo "9. 查看钱包私钥"
    echo "0. 退出"

    read -p "请输入您的选择：" choice

    case $choice in
        1) modify_rpc ;;
        2) modify_gas ;;
        3) start_mining ;;
        4) stop_mining ;;
        5) start_claim ;;
        6) stop_claim ;;
        7) query_amount ;;
        8) update_ore_cli ;;
        9) view_wallet_private_key ;;
        0) echo "退出脚本。"; exit ;;
        *) echo "无效的选择，请输入有效的选项。" ;;
    esac
}

# 主执行开始
while true; do
    main_menu
done
"""
        client.exec_command(f'echo "{run_script}" > ~/run.sh && chmod +x ~/run.sh')
        # 打印所有钱包文件的内容
        print("打印钱包文件内容:")
        for i in range(1, num_wallets + 1):
            wallet_file_path = f"~/.config/solana/{i}.json"
            cat_command = f"cat {wallet_file_path}"
            stdin, stdout, stderr = client.exec_command(cat_command, get_pty=True)
            exit_status = stdout.channel.recv_exit_status()  # 等待命令执行完成
            # 打印文件内容
            print(f"钱包{i}的内容:")
            print("".join(stdout.readlines()))
            print("错误信息:")
            print("".join(stderr.readlines()))

        # 关闭SSH链接
        client.close()

    except Exception as e:
        print("错误信息:", str(e))


# hostname = input("请输入主机名: ")
# username = input("请输入用户名: ")
# password = input("请输入密码: ")
# port = int(input("请输入SSH端口号 (默认为22): ") or 22)

hostname = "127.0.0.1"
username = ""
password = ""
port = 7890

ssh_exec_commands(hostname, username, password, port)
