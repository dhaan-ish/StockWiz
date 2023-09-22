from gradio_client import Client

client = Client("https://wizzseen-stock.hf.space/")
result = client.predict(
                "132,122,234,55555",    # str in 'features' Textbox component
                api_name="/predict"
)
print(result)