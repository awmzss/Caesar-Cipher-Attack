import heapq
import requests
import concurrent.futures
from bs4 import BeautifulSoup
from string import ascii_lowercase

alphabet = ascii_lowercase

def check_word_existence(word):
    url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        return 1 if response.status_code == 200 else 0
    except requests.RequestException:
        return 0  # If request fails, assume word is not valid

def caesar_attack(ciphertext, key):
    ciphertext = ciphertext.lower()
    plaintext = ""
    for char in ciphertext:
        if char in alphabet:
            plaintext += alphabet[(alphabet.index(char) - key) % 26]
        else:
            plaintext += char
    return plaintext

def bruteforce(ciphertext):
    pq = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_key = {executor.submit(process_key, ciphertext, key): key for key in range(26)}
        for future in concurrent.futures.as_completed(future_to_key):
            result = future.result()
            heapq.heappush(pq, result)
    return pq

def process_key(ciphertext, key):
    plaintext = caesar_attack(ciphertext, key)
    words = plaintext.split()
    score = sum(check_word_existence(word) for word in words)
    return (-score, plaintext) if score >= 0 else None

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    ciphertext = input("Enter the cipher text: ").strip()
    if not ciphertext:
        print("Error: Cipher text cannot be empty.")
    else:
        top = get_valid_input("Output the top {X} possibilities, Enter X [1, 26]: ", 1, 26)
        results = bruteforce(ciphertext)
        for i in range(min(top, len(results))):
            _, item = heapq.heappop(results)
            print(f"top{i+1}: {item}")
