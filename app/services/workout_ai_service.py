from openai import OpenAI
from config import Config


class WorkoutAIService:

    @staticmethod
    def generate_workout(energy_level, body_part, goal, workout_time, weight, height, fitness_level, gym_experience):

        client = OpenAI(api_key=Config.OPEN_API_KEY)

        prompt = f"""You are an elite personal trainer.Create a highly detailed workout plan.
User Information:

Body Part:
{body_part}

Goal:
{goal}

Workout Time:
{workout_time}

Requirements:

Create a complete workout.

Include:

Warmup

Exercise name

Sets

Reps

Rest periods

Exercise order

Cooldown

Explain why each exercise was chosen.

Do not recommend generic workouts.

Act like a real trainer coaching a client.
"""

        response = client.responses.create(
            model="gpt-5.4-mini",
            input=prompt
        )

        return response.output_text