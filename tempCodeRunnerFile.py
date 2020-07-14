import pyshorteners

url = input("Enter Url>>>")

print("Url After Shortening-->>",pyshorteners.Shortener().tinyurl.short(url))