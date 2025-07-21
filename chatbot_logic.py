def get_chat_response(message, stream):
    message = message.lower()

    # Basic hardcoded logic based on stream
    if stream == 'cs':
        return "Based on your CS stream, you might explore careers like Software Developer, Data Scientist, or AI/ML Engineer."
    elif stream == 'bio':
        return "Since you're in the Biology stream, consider becoming a Doctor, Biotechnologist, Pharmacist, or Research Scientist."
    elif stream == 'arts':
        return "For Arts, fields like Psychology, Journalism, Law, or Design could be great for you."
    else:
        return "Tell me more about your interests so I can guide you better!"
