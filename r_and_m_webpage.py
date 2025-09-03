import requests

# Base URL
url = "https://rickandmortyapi.com/api/character"

# Request API data
response = requests.get(url)
data = response.json()

# Start HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
</head>
<body>
"""



# Add character cards
# for char in data["results"]:
#     html_content += f"""
#     <div>
#         <img src="{char['image']}" width = "100" alt="{char['name']}">
#         <h2>{char['name']}</h2>
#         <p><strong>Status:</strong> {char['status']}</p>
#         <p><strong>Species:</strong> {char['species']}</p>
#         <p><strong>Origin:</strong> {char['origin']['name']}</p>
#     </div>
#     """
# # End character cards

for char in data["results"]:
    html_content += f"""
    <main>
    <div>
        <h1>Derived from The Rick and Morty API</h1>
        <h2>{char['name']}</h2>  
        <img src="{char['image']}" width = "100" alt="{char['name']}">
        <ul>
            <li>Status: {char['status']}</li>
            <li>Species: {char['species']}</li>
            <li>Location: {char['location']['name']}</li>
            <li>Type: {char['type']}</li>
            <li>Gender: {char['gender']}</li>
        </ul>
    </div>
        Recorded on <strong>2017-11-04</strong>
        </main>
        <footer>
         <p><a href="{char['url']}">See more {char['name']} details here!</a></p>
         </footer>
    """
# End character cards


html_content += """
</body>
</html>
"""
# End HTML structure

# Write to HTML file
with open("rick_and_morty.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: rick_and_morty_strong.html")

