import { Wallet } from '@project-serum/anchor'
import { Connection, Keypair, VersionedTransaction,LAMPORTS_PER_SOL } from '@solana/web3.js'
import bs58 from 'bs58';
import fetch from 'node-fetch'
import sleep from './util/sleep.js'
const inputToken = 'So11111111111111111111111111111111111111112'
const outputToken = '7EYnhQoR9YM3N7UoaKRoA44Uy8JeaZV3qyouov87awMs'
const amount = '50000000'
const fromAddress = '2kpJ5QRh16aRQ4oLZ5LnucHFDAZtEFz6omqWWMzDSNrx'
const slippage = 0.5
// GMGN API domain
const API_HOST = 'https://gmgn.ai'
async function main() {
    // Wallet initialization, skip this step if using Phantom
    const wallet = new Wallet(Keypair.fromSecretKey(bs58.decode(process.env.PRIVATE_KEY || '')))
    console.log(`wallet address: ${wallet.publicKey.toString()}`)
    // Get quote and unsigned transaction
    const quoteUrl = `${AdPI_HOST}/defi/router/v1/sol/tx/get_swap_route?token_in_address=${inputToken}&token_out_address=${outputToken}&in_amount=${amount}&from_address=${fromAddress}&slippage=${slippage}`
    let route = await fetch(quoteUrl)
    route = await route.json()
    console.log(route)
    // Sign transaction
    const swapTransactionBuf = route.data.quote.contextSlot ? Buffer.from(route.data.raw_tx.swapTransaction, 'base64') : bs58.decode(route.data.raw_tx.swapTransaction)
    const transaction = VersionedTransaction.deserialize(swapTransactionBuf)
    transaction.sign([wallet.payer])
    const signedTx = bs58.encode(transaction.serialize())
    console.log(signedTx)
    // Submit transaction
    let res = await fetch(`${API_HOST}/defi/router/v1/sol/tx/submit_signed_transaction`,
        {
            method: 'POST',
            headers: {'content-type': 'application/json'},
            body: JSON.stringify(
                {
                    "signed_tx": signedTx
                }
            )
        })
    res = await res.json()
    console.log(res)
    // Check transaction status
    // If the transaction is successful, success returns true
    // If is does not go through，expired=true will be returned after 60 seconds
    while (true) {
        const hash =  res.data.hash
        const lastValidBlockHeight = route.data.raw_tx.lastValidBlockHeight
        const statusUrl = `${API_HOST}/defi/router/v1/sol/tx/get_transaction_status?hash=${hash}&last_valid_height=${lastValidBlockHeight}`
        let status = await fetch(statusUrl)
        status = await status.json()
        console.log(status)
        if (status && (status.data.success === true || status.data.expired === true))
        break
        await sleep(1000)
    }
}
main()
