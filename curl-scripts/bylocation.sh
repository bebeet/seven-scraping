curl --location --request POST 'https://www.7eleven.co.th/api/v1/Store/GetStoreByCurrentLocation' \
--header 'Accept: application/json, text/plain, */*' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36' \
--header 'Content-Type: application/json;charset=UTF-8' \
--header 'Origin: https://www.7eleven.co.th' \
--data-raw '{"latitude":13.723,"longitude":100.571}'  
	