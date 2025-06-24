def get_bot_response(message):
    message = message.lower()

    if "software" in message:
        return "You can become a Software Engineer. Start with B.Tech or BCA, then learn DSA, Git, and do projects."
    elif "bio" in message:
        return "You can choose fields like MBBS, BDS, B.Pharm, or Biomedical Engineering."
    elif "arts" in message:
        return "Options include BA in Literature, Sociology, Journalism, or even UPSC preparation."
    else:
        return "Please specify your interest (e.g., software, bio, arts), and I'll guide you."
