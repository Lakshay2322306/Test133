FROM libretranslate/libretranslate

# Optimized for Render free tier
CMD ["--host", "0.0.0.0", 
     "--port", "10000",
     "--load-only", "en,es,fr,de",  # Limit loaded languages
     "--threads", "2"]  # Reduce memory usage
