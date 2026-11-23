# REST API & Postman Cheat Sheet

## 1. The API Simulator

- **Base URL:** `http://library.demo.local/api/v1`
- **Web Interface/Docs:** Open `http://library.demo.local` in a browser to view the interactive OpenAPI/Swagger documentation.

## 2. Authentication: Getting a Token

Most API calls require a token. Get one by sending a `POST` request to the login endpoint.

- **Endpoint:** `POST /loginViaBasic`
- **Auth Type:** **Basic Auth**
- **Username:** `cisco`
- **Password:** `Cisco123!`
- **Response:** A JSON response containing a token, such as `{"token": "cisco|..."}`.

The token expires and must be sent in the header for future authenticated requests.

### Using the Token

- **Header Key:** `X-API-KEY`
- **Header Value:** `cisco|YourTokenStringHere`

## 3. API Endpoints & Methods

### `GET /books`: List All Books

- **URL:** `http://library.demo.local/api/v1/books`
- **Optional query parameters:**
  - `includeISBN=true`: Add ISBN to the response.
  - `sortBy=author`: Sort results by author.

Example:

```text
http://library.demo.local/api/v1/books?includeISBN=true&sortBy=author
```

### `GET /books/{id}`: Get a Specific Book

- **URL:** `http://library.demo.local/api/v1/books/4`
- **Authentication:** Required.

### `POST /books`: Add a New Book

- **URL:** `http://library.demo.local/api/v1/books`
- **Authentication:** Required.
- **Body:**

```json
{
  "id": 4,
  "title": "IPv6 Fundamentals",
  "author": "Rick Graziani"
}
```

### `DELETE /books/{id}`: Remove a Book

- **URL:** `http://library.demo.local/api/v1/books/4`
- **Authentication:** Required.

## 4. Using Postman

1. **Create a request:** Click the `+` tab.
2. **Set method and URL:** Choose `GET`, `POST`, or `DELETE`, then paste the URL.
3. **Add authentication for login:**
   - Open the **Authorization** tab.
   - Set **Type** to **Basic Auth**.
   - Enter the username and password.
4. **Add authentication for a token:**
   - Open the **Authorization** tab.
   - Set **Type** to **API Key**.
   - Set **Key** to `X-API-KEY`.
   - Set **Value** to `cisco|your_token_here`.
   - Set **Add to** to **Header**.
5. **Add a JSON body for `POST`:**
   - Open the **Body** tab.
   - Select **raw**.
   - Change the format from **Text** to **JSON**.
   - Paste the JSON payload.
6. **Add query parameters for `GET`:**
   - Open the **Params** tab.
   - Enter the key `includeISBN` and value `true`.
   - Postman updates the URL with `?` and `&` automatically.

## 5. Using `curl`

### GET with Parameters

```bash
curl -X GET "http://library.demo.local/api/v1/books?includeISBN=true&sortBy=author" \
  -H "accept: application/json"
```

### POST: Login

```bash
curl -X POST "http://library.demo.local/api/v1/loginViaBasic" \
  -u "cisco:Cisco123!"
```

### POST: Add a Book with Authentication

```bash
curl -X POST "http://library.demo.local/api/v1/books" \
  -H "X-API-KEY: cisco|YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"id": 4, "title": "IPv6 Fundamentals", "author": "Rick Graziani"}'
```

## 6. Troubleshooting

- **401 Unauthorized:** The `X-API-KEY` header is missing, the token expired, or extra spaces were copied into the token.
- **200 OK:** The request succeeded.
- **400 Bad Request:** The JSON body may be malformed or required parameters may be missing.

# Python REST API Integration: Graphhopper

## 1. Core Modules

Use `requests` to make API calls and `urllib.parse` to format URLs.

```python
import requests
import urllib.parse
```

## 2. Building the API URL

Use `urllib.parse.urlencode` to format query parameters so that spaces, commas, and other special characters are URL-encoded correctly.

- **Base URL:** `https://graphhopper.com/api/1/geocode?`

```python
location = "Washington, D.C."
key = "YOUR_API_KEY"
geocode_url = "https://graphhopper.com/api/1/geocode?"

# Converts the location into a URL-safe query value.
url = geocode_url + urllib.parse.urlencode({
	"q": location,
	"limit": "1",
	"key": key,
})
```

## 3. Making the Request and Checking Status

Always check `status_code` before trying to read the response data.

```python
replydata = requests.get(url)
json_status = replydata.status_code

if json_status == 200:
	json_data = replydata.json()  # Converts the response to a Python dictionary.
	print("Success!")
else:
	print("API call failed.")
```

## 4. Navigating JSON Data

The Graphhopper Geocoding API returns a nested dictionary. Extract coordinates like this:

```python
# Example shape: {'hits': [{'point': {'lat': 38.8, 'lng': -77.0}, ...}]}
lat = json_data["hits"][0]["point"]["lat"]
lng = json_data["hits"][0]["point"]["lng"]
```

## 5. The Geocoding Function

Wrapping the API logic in a function makes it reusable for both the starting location and destination.

```python
def geocoding(location, key):
	# Handle empty input.
	while location == "":
		location = input("Enter the location again: ")

	# Build the URL and get the data.
	geocode_url = "https://graphhopper.com/api/1/geocode?"
	url = geocode_url + urllib.parse.urlencode({
		"q": location,
		"limit": "1",
		"key": key,
	})

	replydata = requests.get(url)
	json_data = replydata.json()
	json_status = replydata.status_code

	if json_status == 200:
		lat = json_data["hits"][0]["point"]["lat"]
		lng = json_data["hits"][0]["point"]["lng"]

		# Cleanly format the location name.
		hit = json_data["hits"][0]
		name = hit["name"]
		country = hit.get("country", "")
		state = hit.get("state", "")

		if state and country:
			new_loc = f"{name}, {state}, {country}"
		elif country:
			new_loc = f"{name}, {country}"
		else:
			new_loc = name

		print(
			f"Geocoding API URL for {new_loc} "
			f"(Location Type: {hit['osm_value']})"
		)
		print(url)
	else:
		lat = "null"
		lng = "null"
		new_loc = location
		print("Error: " + json_data["message"])

	return json_status, lat, lng, new_loc
```

## 6. Main Loop and User Input

This loop asks for locations until the user enters `quit` or `q`.

```python
while True:
	loc1 = input("Starting Location: ")
	if loc1.lower() == "quit" or loc1.lower() == "q":
		break

	orig = geocoding(loc1, key)
	print(orig)

	loc2 = input("Destination: ")
	if loc2.lower() == "quit" or loc2.lower() == "q":
		break

	dest = geocoding(loc2, key)
	print(dest)
```

## 7. Key Takeaways

- **Never hardcode coordinates:** Use the Geocoding API to look them up dynamically.
- **Use `urllib.parse`:** APIs can reject URLs containing raw spaces or invalid characters.
- **Check `status_code == 200`:** This prevents failures when the API key is invalid or the server is unavailable.
- **Use `.get("key", "default")`:** Optional JSON keys such as `state` may not exist, and `.get()` prevents `KeyError` crashes.
