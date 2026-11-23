
# Resolution in First Order Logic

# Literal format: (sign, predicate, arguments)
# Sign: 1 = Positive, -1 = Negative

def L(sign, pred, *args):
    return (sign, pred, args)


# Apply substitution
def substitute(literal, subs):
    sign, pred, args = literal
    new_args = []

    for arg in args:
        while arg in subs:
            arg = subs[arg]
        new_args.append(arg)

    return (sign, pred, tuple(new_args))


# Unification
def unify(a, b, subs):
    a = substitute(a, subs)[2][0]
    b = substitute(b, subs)[2][0]

    if a == b:
        return True

    if a.startswith("?"):
        subs[a] = b
        return True

    if b.startswith("?"):
        subs[b] = a
        return True

    return False


# Resolution function
def resolve(c1, c2):

    for l1 in c1:
        for l2 in c2:

            if l1[0] == -l2[0] and l1[1] == l2[1]:
                if len(l1[2]) != len(l2[2]):
                    continue

                subs = {}
                valid = True

                for a, b in zip(l1[2], l2[2]):
                    if a != b:
                        if a.startswith("?"):
                            subs[a] = b
                        elif b.startswith("?"):
                            subs[b] = a
                        else:
                            valid = False
                            break

                if valid:
                    result = []

                    for lit in c1:
                        if lit != l1:
                            result.append(substitute(lit, subs))

                    for lit in c2:
                        if lit != l2:
                            result.append(substitute(lit, subs))

                    return result

    return None


# Knowledge Base in CNF

C1 = [L(-1, "Food", "?x"),
      L(1, "Likes", "John", "?x")]

C2 = [L(1, "Food", "Apple")]

C3 = [L(1, "Food", "Vegetables")]

C4 = [L(-1, "Eats", "?x", "?y"),
      L(-1, "NotKilled", "?x"),
      L(1, "Food", "?y")]

C5 = [L(1, "Eats", "Anil", "Peanuts")]

C6 = [L(1, "Alive", "Anil")]

C7 = [L(-1, "Eats", "Anil", "?x"),
      L(1, "Eats", "Harry", "?x")]

C8 = [L(-1, "Alive", "?x"),
      L(1, "NotKilled", "?x")]

C9 = [L(-1, "NotKilled", "?x"),
      L(1, "Alive", "?x")]

# Negation of the query
C10 = [L(-1, "Likes", "John", "Peanuts")]


print("Knowledge Base Created Successfully")

# Step 1: Alive(Anil) and Alive -> NotKilled
R1 = resolve(C8, C6)
print("Step 1:", R1)

# Step 2: Eats(Anil, Peanuts) and food rule
R2 = resolve(C4, C5)
print("Step 2:", R2)

# Step 3: Resolve with NotKilled(Anil)
R3 = resolve(R2, R1)
print("Step 3:", R3)

# Step 4: Food(Peanuts) and John likes all food
R4 = resolve(C1, R3)
print("Step 4:", R4)

# Step 5: Resolve with negated query
R5 = resolve(R4, C10)
print("Step 5:", R5)

# Check result
if R5 == []:
    print("\nEmpty Clause Derived!")
    print("Query PROVED: John likes Peanuts.")
else:
    print("\nQuery cannot be proved.")
