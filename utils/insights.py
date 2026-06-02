import random

def generate_insight(df):
    # Check if dataframe is empty
    if df.empty:
        return "No data available for this region."
    
    # Check if required columns exist
    required_cols = {"product", "total_sales"}
    if not required_cols.issubset(df.columns):
        return "⚠️ Required columns 'product' or 'total_sales' are missing."
    
    # Drop NaN values before calculation
    df = df.dropna(subset=["product", "total_sales"])
    
    if df.empty:
        return "⚠️ No valid data after removing nulls."
    
    # Calculations
    top_product = df.groupby("product")["total_sales"].sum().idxmax()
    total = df["total_sales"].sum()
    avg_order = df["total_sales"].mean()

    # Return all insights instead of random one
    insights = [
        f"💰 Total sales in this region: ${total:.2f}",
        f"🔥 Best-seller: {top_product}",
        f"📦 Average order value: ${avg_order:.2f}"
    ]
    
    return "\n".join(insights)


# corrections done are:-
# ✅ Added column existence check
# ✅ Added null drop before calculations
# ✅ Returns all 3 insights instead of random 1 — more useful for a dashboard


# import random

# def generate_insight(df):
#     if df.empty:
#         return "No data available for this region."

#     top_product = df.groupby("product")["total_sales"].sum().idxmax()
#     total = df["total_sales"].sum()
#     avg_order = df["total_sales"].mean()

#     options = [
#         f"💰 Total sales in this region: ${total:.2f}",
#         f"🔥 Best-seller: {top_product}",
#         f"📦 Average order value: ${avg_order:.2f}"
#     ]
#     return random.choice(options)
