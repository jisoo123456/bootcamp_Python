#5.2(다음과 같은 형식으로 각 리스트의 질문과 답 출력)

question=[
    "We don't serve strings around here. Are you a string",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis!' 'Boom!' 'Bah!'?"
]

answers=[
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

for i in range(0, len(question)):
    print(question[i], answers[i])