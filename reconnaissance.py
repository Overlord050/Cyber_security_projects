import os
import whois
import shodan
import requests
from PIL import Image
from PIL.ExifTags import TAGS
import argparse

SHODAN_API_KEY="AObjXVXeLRdBKlIQAO1neQvtntphWXJ9"

 
# Make sure to set the SHODAN_API_KEY in your visual code studio

# WHOIS Lookup
def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        # Enhanced WHOIS info output for relevant details
        return {
            "Registrar": w.registrar,
            "Creation Date": w.creation_date,
            "Expiration Date": w.expiration_date,
            "Domain Status": w.status
        }
    except Exception as e:
        return f"Error fetching WHOIS data: {e}"

# Shodan IP Lookup function
def shodan_lookup(ip):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        result = api.host(ip)
        return result
    except shodan.APIError as e:
        # Improved error handling for rate limits
        if "rate limit" in str(e).lower():
            return "API rate limit exceeded. Try again later."
        return f"Shodan Error: {e}"

# Metadata Extraction from Image (EXIF data)
def extract_metadata(image_path):
    try:
        img = Image.open(image_path)
        metadata = {}
        if hasattr(img, '_getexif'):
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    metadata[TAGS.get(tag)] = value
            else:
                return "No EXIF data found"
        return metadata
    except Exception as e:
        return f"Error extracting metadata: {e}"

# Main function to handle all logic
def main():
    # Setup argument parsing
    parser = argparse.ArgumentParser(description="Automated OSINT Reconnaissance Tool")
    
    # Arguments for different checks
    parser.add_argument("--domain", type=str, help="Perform WHOIS lookup on a domain")
    parser.add_argument("--ip", type=str, help="Perform Shodan reconnaissance on an IP")
    parser.add_argument("--image", type=str, help="Extract metadata from an image file")
    
    # Parse arguments
    args = parser.parse_args()

    if args.domain:
        print(f"\nWHOIS Lookup for Domain: {args.domain}")
        print(get_whois_info(args.domain))
    
    if args.ip:
        print(f"\nShodan Lookup for IP: {args.ip}")
        print(shodan_lookup(args.ip))
    
    if args.image:
        print(f"\nExtracting Metadata from Image: {args.image}")
        print(extract_metadata(args.image))

# Entry point
if __name__ == "__main__":
    main()
