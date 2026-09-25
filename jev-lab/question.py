from typesafe_sdk import Noul, Score

TOPICS = {
    "Comfort": "comfort",
    "Fit & Size": "fit_and_size",
    "Design": "design",
    "Material": "material",
    "Durability": "durability",
    "Sole & Grip": "sole_and_grip",
    "Breathability": "breathability",
    "Weight": "weight",
    "Quality": "quality",
    "Value for Money": "value_for_money",
}

SATISFACTION_LEVELS = [
    "Very dissatisfied",                                               # 1 star
    "Dissatisfied",                                                    # 2 stars
    "Neither satisfied nor dissatisfied, or balanced mixed feedback",  # 3 stars
    "Satisfied",                                                       # 4 stars
    "Very satisfied",                                                  # 5 stars
]

QUESTIONS = {
    # Comfort
    "comfort_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about how comfortable the shoes are when wearing or walking?"
    ),
    "comfort_rating": Score(
        instructions="How satisfied is the reviewer with the comfort of the shoes?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Fit & Size
    "fit_and_size_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the shoe's size, fit, or how well it fits their feet?"
    ),
    "fit_and_size_rating": Score(
        instructions="How satisfied is the reviewer with the shoe's fit and size?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Design
    "design_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the shoes' appearance, style, shape, or overall design?"
    ),
    "design_rating": Score(
        instructions="How satisfied is the reviewer with the shoe's design?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Material
    "material_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the materials used in the shoes, such as leather, fabric, mesh, or synthetic material?"
    ),
    "material_rating": Score(
        instructions="How satisfied is the reviewer with the shoe's material?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Durability
    "durability_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about how long the shoes last, wear and tear, or how well they hold up over time?"
    ),
    "durability_rating": Score(
        instructions="How satisfied is the reviewer with the durability of the shoes?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Sole & Grip
    "sole_and_grip_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the shoe's sole, traction, grip, cushioning, or stability while walking?"
    ),
    "sole_and_grip_rating": Score(
        instructions="How satisfied is the reviewer with the sole, grip, and traction of the shoes?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Breathability
    "breathability_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about how well the shoes allow air to flow or keep the feet cool and dry?"
    ),
    "breathability_rating": Score(
        instructions="How satisfied is the reviewer with the breathability of the shoes?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Weight
    "weight_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about whether the shoes feel lightweight, heavy, or easy to wear?"
    ),
    "weight_rating": Score(
        instructions="How satisfied is the reviewer with the weight of the shoes?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Quality
    "quality_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the overall quality, finishing, stitching, construction, or workmanship of the shoes?"
    ),
    "quality_rating": Score(
        instructions="How satisfied is the reviewer with the overall quality of the shoes?",
        criteria=SATISFACTION_LEVELS,
    ),

    # Value for Money
    "value_for_money_mentioned": Noul(
        instructions="Does the reviewer express whether the shoes are worth their price or provide good value for the money?"
    ),
    "value_for_money_rating": Score(
        instructions="How satisfied is the reviewer with the value for money of the shoes?",
        criteria=SATISFACTION_LEVELS,
    ),
}