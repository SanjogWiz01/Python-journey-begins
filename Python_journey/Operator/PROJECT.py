# Smart Calculator using Operators

print("=== Smart Calculator ===")
print("Operations: +  -  *  /  //  %  **")
print("Type 'exit' to stop\n")

while True:
    expr = input("Enter expression (e.g., 5 + 3): ")

    if expr.lower() == "exit":
        print("Goodbye!")
        break

    try:
        result = eval(expr)  # safely evaluates expression
        print("Result:", result)
    except Exception as e:
        print("Invalid input:", e)
# --- IGNORE ----------------------------------------------
# --- -------------------IGNORE ------------------------------