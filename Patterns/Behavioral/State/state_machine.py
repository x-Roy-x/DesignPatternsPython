from enum import Enum, auto


class State(Enum):

    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()


class Trigger(Enum):

    CALL_DIALED = auto()
    HUNG_UP = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


if __name__ == '__main__':
    rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.OFF_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD)
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK)
        ]
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f"The phone is currently {state}")

        triggers = rules[state]
        for position in range(len(triggers)):
            trigger = triggers[position][0]
            print(f"{position}: {trigger}")

        selected_trigger_position = int(input("Select a trigger position: "))
        state = rules[state][selected_trigger_position][1]

    print("Whe have done using phone")


