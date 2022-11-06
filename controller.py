from repository import get_user_name, execute_eight_ball_program


def main():
    progress = True
    username = get_user_name(progress)
    execute_eight_ball_program(progress, username)


if __name__ == "__main__":
    main()
