Trace Data
---
In any system where data is regularly imported from a 3rd party system, the data goes through mulitple stages:
1. ingress (pulling the data in)
2. transform (normalize the data to match your internal schema)
3. validation (during the transform process, if you don't have a way to map the external data to your internal data, you put it aside in an error table)
4. distribution (send to a bunch of your other apps), egress (exit out of your system)

This project's goal is to try to simulate how much data makes it from ingress all the way to egress, and if it fails, how to figure out what failed, when, and where.

For the initial setup (Python, python libraries, and MySQL) run
```
pip install -r requirements.txt
```

To generate the data, run the Python script `database\gen_monthly_view.py`. This generates a bunch of random data and adds it to the SQL database.