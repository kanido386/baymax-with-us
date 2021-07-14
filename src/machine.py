from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        # states=["user", "state1", "state2"],
        states=["user", "youtube", "kkbox", "kkbox_playlist", "exercise", "fact_checking", "game_options", "game_leisure", "game_challenge", "weather", "feature_request", "feature_show"],
        transitions=[
            { "trigger": "advance", "source": "user", "dest": "youtube", "conditions": "is_going_to_youtube" },
            { "trigger": "advance", "source": "user", "dest": "kkbox", "conditions": "is_going_to_kkbox" },
            { "trigger": "advance", "source": "user", "dest": "kkbox_playlist", "conditions": "is_going_to_kkbox_playlist" },
            { "trigger": "advance", "source": "user", "dest": "exercise", "conditions": "is_going_to_exercise" },
            { "trigger": "advance", "source": "user", "dest": "fact_checking", "conditions": "is_going_to_fact_checking" },
            { "trigger": "advance", "source": "user", "dest": "game_options", "conditions": "is_going_to_game_options" },
            { "trigger": "advance", "source": "user", "dest": "game_leisure", "conditions": "is_going_to_game_leisure" },
            { "trigger": "advance", "source": "user", "dest": "game_challenge", "conditions": "is_going_to_game_challenge" },
            { "trigger": "advance", "source": "user", "dest": "weather", "conditions": "is_going_to_weather" },
            { "trigger": "advance", "source": "user", "dest": "feature_request", "conditions": "is_going_to_feature_request" },
            { "trigger": "advance", "source": "user", "dest": "feature_show", "conditions": "is_going_to_feature_show" },

            # { "trigger": "advance", "source": "user", "dest": "state1", "conditions": "is_going_to_state1" },
            # { "trigger": "advance", "source": "user", "dest": "state2", "conditions": "is_going_to_state2" },
            # { "trigger": "go_back", "source": ["state1", "state2"], "dest": "user" },
            { "trigger": "go_back", "source": ["youtube", "kkbox", "kkbox_playlist", "exercise", "fact_checking", "game_options", "game_leisure", "game_challenge", "weather", "feature_request", "feature_show"], "dest": "user" },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine