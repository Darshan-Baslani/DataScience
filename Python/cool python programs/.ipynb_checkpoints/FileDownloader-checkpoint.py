{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4611c99f-d89d-43a8-903c-cb7bc563cf9d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import requests\n",
    "import math\n",
    "from tqdm import tqdm\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
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
   "execution_count": 16,
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
   "execution_count": 17,
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
   "execution_count": 18,
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
   "execution_count": 19,
   "id": "5bb4b0cf-ceda-4c7e-9595-f9e96065b277",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████████████████████████████████████████████████████████████████████████████| 12/12 [00:06<00:00,  1.99it/s]"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Downloaded Successfully!\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "if response.status_code == 200:\n",
    "    with open('file.pdf', 'wb') as file:\n",
    "        for chunk in tqdm(response.iter_content(chunk_size=chunk_size) , total=n):\n",
    "            time.sleep(0.5)\n",
    "            file.write(chunk)\n",
    "    print('Downloaded Successfully!')\n",
    "else:\n",
    "    print('Error!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91af8bf5-1825-4255-a1c3-fdba0e7f6e12",
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
