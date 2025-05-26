from flask import Flask, render_template, redirect, url_for
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
app = Flask(__name__)

key_vault_url = "https://identity-solution.vault.azure.net/"
credential = DefaultAzureCredential()
secure_client = SecretClient(vault_url=key_vault_url, credential=credential)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/identity')
def secure():
    try:
        secret = secure_client.get_secret("Azure-identity-key").value 
    except Exception as e:
        secret = f"Error retrieving secret: {str(e)}"
    return render_template('secure.html', secret=secret)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

