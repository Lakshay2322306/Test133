FROM libretranslate/libretranslate

# Enable CORS and set the correct port
CMD ["--host", "0.0.0.0", "--port", "10000", "--cors"]
