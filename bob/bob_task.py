# Task from https://exercism.org/tracks/python/exercises/bob
import logging

logging.basicConfig(level=logging.INFO)

POSSIBLE_ANSWERS = {
    "say_nothing": "Fine. Be that way!",
    "question": "Sure.",
    "yell_question": "Calm down, I know what I'm doing!",
    "yell": "Whoa, chill out!",
    "else": "Whatever."
}


def response(hey_bob: str):
    try:
        lowercase_hey = hey_bob.lower()
        uppercase_hey = hey_bob.upper()
        hey_bob = hey_bob.strip()
        # case 1: empty string
        if hey_bob == "":
            return POSSIBLE_ANSWERS.get("say_nothing")
        # case 2: uppercase question
        elif hey_bob.endswith("?") and hey_bob == uppercase_hey:
            return POSSIBLE_ANSWERS.get("yell_question")
        # case 3: non-uppercase question
        elif hey_bob.endswith("?"):
            return POSSIBLE_ANSWERS.get("question")
        # case 4: uppercase string
        elif hey_bob == uppercase_hey:
            return POSSIBLE_ANSWERS.get("yell")
        # other cases or non-string provided
        return POSSIBLE_ANSWERS.get("else")
    except:
        return POSSIBLE_ANSWERS.get("else")


def main():
    logging.info(response("Tom-ay-to, tom-aaaah-to."))  # Whatever.
    logging.info(response("WATCH OUT!"))  # Whoa, chill out!
    logging.info(response("FCECDFCAAB"))  # Whoa, chill out!
    logging.info(response("You are, what, like 15?"))  # Sure.
    logging.info(response("WHAT?"))  # Calm down, I know what I'm doing!
    logging.info(response("  "))  # Fine. Be that way!


if __name__ == "__main__":
    main()
