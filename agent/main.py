


# 💻 3. Python CLI Agent (BONUS — VERY IMPORTANT)


import json

# Load tree
with open("../tree/reflection-tree.json") as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}

state = {
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0},
    "axis3": {"altrocentric": 0, "self": 0},
    "answers": {}
}

def get_dominant(axis):
    return max(state[axis], key=state[axis].get)

def run():
    current = "START"

    while True:
        node = nodes[current]
        print("\n" + node["text"])

        if node["type"] == "end":
            break

        elif node["type"] == "question":
            options = node["options"]

            for i, opt in enumerate(options):
                print(f"{i+1}. {opt['text']}")

            choice = int(input("Choose: ")) - 1
            selected = options[choice]

            # Save answer
            state["answers"][node["id"]] = selected["text"]

            # Update signal
            if "signal" in selected:
                axis, val = selected["signal"].split(":")
                state[axis][val] += 1

            current = selected["target"]

        elif node["type"] in ["reflection", "bridge"]:
            input("Press Enter to continue...")
            current = node["next"]

        elif node["type"] == "decision":
            if "axis1" in node:
                current = node[get_dominant("axis1")]
            elif "axis2" in node:
                current = node[get_dominant("axis2")]
            elif "axis3" in node:
                current = node[get_dominant("axis3")]

        elif node["type"] == "summary":
            a1 = get_dominant("axis1")
            a2 = get_dominant("axis2")
            a3 = get_dominant("axis3")

            print(f"\nSummary:")
            print(f"You leaned {a1} in agency, {a2} in contribution, and {a3} in perspective.")

            current = node["next"]


if __name__ == "__main__":
    run()