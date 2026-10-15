def main() -> None:
    input_tokens = int(input("Enter the number of input tokens: "))
    output_tokens = int(input("Enter the number of output tokens: "))
    input_price_per_million = 2
    output_price_per_million = 8

    total_cost = calculate_cost(
        input_tokens,
        output_tokens,
        input_price_per_million,
        output_price_per_million,
    )

    print(f"Total cost: ${total_cost:.6f}")

def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    input_price_per_million: float,
    output_price_per_million: float,
) -> float:
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("Number of tokens cannot be negative.")    
    input_cost = input_tokens / 1_000_000 * input_price_per_million
    output_cost = output_tokens / 1_000_000 * output_price_per_million
    total_cost = input_cost + output_cost
    return total_cost