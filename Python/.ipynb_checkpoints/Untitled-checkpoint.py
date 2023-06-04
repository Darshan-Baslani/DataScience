{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4611c99f-d89d-43a8-903c-cb7bc563cf9d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import requests\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "67813677-0a5c-4f27-9d9d-3deb868b1635",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "url = 'https://www.africau.edu/images/default/sample.pdf'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "37de85ee-d0fe-44ec-bc82-96a1c67d4999",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "response = requests.get(url,stream = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b4598474-273c-429d-b0f4-e78b1961cc99",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "chunk_size = 256 # bytes of data to be processed at a time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "683655df-1897-47b7-a6c1-1f582eb81a49",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# n is no of times the loop will run to download the content, as it is downloading the content in pieces\n",
    "n = math.ceil(int(response.headers['Content-Length']) / chunk_size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5bb4b0cf-ceda-4c7e-9595-f9e96065b277",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "StreamConsumedError",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStreamConsumedError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[18], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mfile.pdf\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mwb\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[1;32m----> 2\u001b[0m     \u001b[38;5;28;01mfor\u001b[39;00m chunk \u001b[38;5;129;01min\u001b[39;00m \u001b[43mresponse\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43miter_content\u001b[49m\u001b[43m(\u001b[49m\u001b[43mchunk_size\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mchunk_size\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[0;32m      3\u001b[0m         file\u001b[38;5;241m.\u001b[39mwrite(chunk)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\requests\\models.py:836\u001b[0m, in \u001b[0;36mResponse.iter_content\u001b[1;34m(self, chunk_size, decode_unicode)\u001b[0m\n\u001b[0;32m    833\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_content_consumed \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[0;32m    835\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_content_consumed \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_content, \u001b[38;5;28mbool\u001b[39m):\n\u001b[1;32m--> 836\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StreamConsumedError()\n\u001b[0;32m    837\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m chunk_size \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(chunk_size, \u001b[38;5;28mint\u001b[39m):\n\u001b[0;32m    838\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\n\u001b[0;32m    839\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mchunk_size must be an int, it is instead a \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mtype\u001b[39m(chunk_size)\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    840\u001b[0m     )\n",
      "\u001b[1;31mStreamConsumedError\u001b[0m: "
     ]
    }
   ],
   "source": [
    "with open('file.pdf', 'wb') as file:\n",
    "    for chunk in response.iter_content(chunk_size=chunk_size):\n",
    "        file.write(chunk)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbec39d7-752e-49eb-967b-16ee40547f8d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
