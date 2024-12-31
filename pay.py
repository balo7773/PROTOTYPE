#!/usr/bin/python3
import requests
import json
import time

headers = {
        'Authorization': f'Bearer sk_test_aff7862c120369380fb5c0dafad7d49bd5b5899c',
                'Content-Type': 'application/json'
        }

def initialize_transaction(amount):
    url = 'https://api.paystack.co/transaction/initialize'
    params = {
                 "email" : "customer@email.com",
                 "amount" : f"{amount}"  # amount will be a dynamic variable depending on purchase price
            }
    res = requests.post(url, headers=headers, data=json.dumps(params))
    if res.status_code == 200:
        data = res.json()
        reference = data['data']['reference']
        print(data)
    else:
        print(f"Error: {res.status_code}, {res.text}")
    return reference

def verify_transaction(reference):
    url = 'https://api.paystack.co/transaction/verify/{}'.format(reference)
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        if data['data']['status'] == 'success':
            print("payment successful")
        else:
            print(f'payment failed: {res.text}')

ref = initialize_transaction(3000000000)
time.sleep(60)
verify_transaction(ref)
