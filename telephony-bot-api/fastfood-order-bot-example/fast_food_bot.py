from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
import os
from typing import List

os.environ["OPENAI_API_KEY"] = 'YOUR-OPENAI-KEY'

llm = ChatOpenAI(model="gpt-4o-mini")


# tool to contain the menu of the restaurant
@tool
def get_menu():
    """Get fast food restaurant menu and price for each item. The price is in dollars
    the menu has burgers and wraps. There are also fries and wedges that can be ordered, and there are 3 different sizes for them as well."""
    menu = {
        "burgers": [
            {"name": "Cheeseburger", "type": "non-veg", "price": 10},
            {"name": "Black Bean Burger", "type": "veg", "price": 12},
            {"name": "Hamburger", "type": "non-veg", "price": 12},
            {"name": "Crispy Chicken Burger", "type": "non-veg", "price": 12},
            {"name": "Veggie Burger", "type": "veg", "price": 12},
            {"name": "Fish Burger", "type": "non-veg", "price": 12},
            {"name": "BBQ Chicken Burger", "type": "non-veg", "price": 12},
            {"name": "Spicy Chicken Burger", "type": "non-veg", "price": 12},
            {"name": "Turkey Burger", "type": "non-veg", "price": 12},
            {"name": "Mushroom Swiss Burger", "type": "veg", "price": 12}
        ],
        "wraps": [
            {"name": "Grilled Chicken Wrap", "type": "non-veg", "price": 10},
            {"name": "Spicy Chicken Wrap", "type": "non-veg", "price": 10},
            {"name": "BBQ Chicken Wrap", "type": "non-veg", "price": 10},
            {"name": "Veggie Wrap", "type": "veg", "price": 10},
            {"name": "Turkey Wrap", "type": "non-veg", "price": 10},
            {"name": "Buffalo Chicken Wrap", "type": "non-veg", "price": 10},
            {"name": "Chicken Caesar Wrap", "type": "non-veg", "price": 10},
            {"name": "Steak Wrap", "type": "non-veg", "price": 10},
            {"name": "Falafel Wrap", "type": "veg", "price": 10},
            {"name": "Hummus Veggie Wrap", "type": "veg", "price": 10}
        ],
        "fries": [
            {"name": "Regular Fries", "sizes": {"Small": 2, "Medium": 3, "Large": 4}},
            {"name": "Curly Fries", "sizes": {"Small": 2.5, "Medium": 3.5, "Large": 4.5}},
            {"name": "Sweet Potato Fries", "sizes": {"Small": 3, "Medium": 4, "Large": 5}},
            {"name": "Waffle Fries", "sizes": {"Small": 3, "Medium": 4, "Large": 5}},
            {"name": "Cajun Fries", "sizes": {"Small": 2.5, "Medium": 3.5, "Large": 4.5}},
            {"name": "Chili Cheese Fries", "sizes": {"Small": 4, "Medium": 5, "Large": 6}},
            {"name": "Garlic Fries", "sizes": {"Small": 3, "Medium": 4, "Large": 5}},
            {"name": "Truffle Fries", "sizes": {"Small": 4.5, "Medium": 5.5, "Large": 6.5}},
            {"name": "Loaded Fries", "sizes": {"Small": 5, "Medium": 6, "Large": 7}},
            {"name": "Cheese Fries", "sizes": {"Small": 3.5, "Medium": 4.5, "Large": 5.5}}
        ],
        "wedges": [
            {"name": "Potato Wedges", "sizes": {"Small": 3, "Medium": 4, "Large": 5}},
            {"name": "Cajun Wedges", "sizes": {"Small": 3.5, "Medium": 4.5, "Large": 5.5}},
            {"name": "Garlic Parmesan Wedges", "sizes": {"Small": 4, "Medium": 5, "Large": 6}},
            {"name": "Buffalo Wedges", "sizes": {"Small": 4, "Medium": 5, "Large": 6}},
            {"name": "Loaded Potato Wedges", "sizes": {"Small": 5, "Medium": 6, "Large": 7}},
            {"name": "Cheesy Wedges", "sizes": {"Small": 3.5, "Medium": 4.5, "Large": 5.5}},
            {"name": "BBQ Wedges", "sizes": {"Small": 4, "Medium": 5, "Large": 6}},
            {"name": "Spicy Wedges", "sizes": {"Small": 3.5, "Medium": 4.5, "Large": 5.5}},
            {"name": "Truffle Wedges", "sizes": {"Small": 4.5, "Medium": 5.5, "Large": 6.5}},
            {"name": "Herb Wedges", "sizes": {"Small": 3.5, "Medium": 4.5, "Large": 5.5}}
        ],
        "drinks": [
            {"name": "Coca-Cola", "size": "Medium", "price": 2},
            {"name": "Pepsi", "size": "Medium", "price": 2},
            {"name": "Sprite", "size": "Medium", "price": 2},
            {"name": "Fanta Orange", "size": "Medium", "price": 2},
            {"name": "Dr. Pepper", "size": "Medium", "price": 2},
            {"name": "Mountain Dew", "size": "Medium", "price": 2},
            {"name": "Root Beer", "size": "Medium", "price": 2},
            {"name": "Iced Tea", "size": "Medium", "price": 2},
            {"name": "Lemonade", "size": "Medium", "price": 2},
            {"name": "Fruit Punch", "size": "Medium", "price": 2}
        ]
    }
    return menu


# list of all add ons for the items
@tool
def get_add_ons():
    """all possible add ons """
    add_ons = [
        {"name": "Extra Cheese", "cost": "1"},
        {"name": "Lettuce", "cost": "1"},
        {"name": "Tomatoes", "cost": "1"},
        {"name": "Bacon", "cost": "1.5"},
        {"name": "Avocado", "cost": "2"},
        {"name": "Jalapenos", "cost": "0.5"},
        {"name": "Extra Patty", "cost": "3"},
        {"name": "Guacamole", "cost": "2"},
        {"name": "Pickles", "cost": "0.5"},
        {"name": "Onions", "cost": "1"},
        {"name": "Mushrooms", "cost": "1.5"},
        {"name": "BBQ Sauce", "cost": "0.5"},
        {"name": "Ranch Dressing", "cost": "0.5"},
        {"name": "Honey Mustard", "cost": "0.5"},
        {"name": "Chipotle Sauce", "cost": "0.5"},
    ]
    return add_ons


# tool to help define what combos are possible
@tool
def get_combos(main_item: str, side: str = None, drink: str = None):
    """Create a meal combo of the user's choice. The user can select a burger or wrap from the menu,
    along with an optional drink and either fries or wedges with that as well, which is also optional."""
    combos = {
        "Main with a Side": {"main_item": main_item, "side": side, "price": 10},
        "Main with a Drink": {"main_item": main_item, "drink": drink, "price": 11},
        "Main with Side and Drink": {"main_item": main_item, "side": side, "drink": drink, "price": 12}
    }
    return combos


class OrderItem(BaseModel):
    item: str = Field(description="the item user ordered from the menu")
    price: float = Field(description="price of the item")
    delete: bool = Field(description="Whether the user want to delete this item")
    quantity: int = Field(description="the amount of items ordered")
    add_on: str = Field(description="the add on item ordered from the menu")
    price_add_on: int = Field(description="the price of the add on items")
    combined_cost: int = Field(description="the cost of the order including the items and the odd ons")


# to store the current order
my_order: List[OrderItem] = []


@tool
def update_order(new_order: OrderItem):
    """This function needs to be called when the user order something, or update their order, or delete something"""
    global my_order

    if new_order.delete:
        # Remove the item from the order
        my_order = [item for item in my_order if not (item.item == new_order.item and item.add_on == new_order.add_on)]
    else:
        item_found = False
        for item in my_order:
            if item.item == new_order.item and item.add_on == new_order.add_on:
                item_found = True
                if new_order.quantity > 0:
                    item.quantity = new_order.quantity
                    item.price = new_order.price
                    item.price_add_on = new_order.price_add_on
                    item.combined_cost = item.price + item.price_add_on
                else:
                    my_order.remove(item)
                break

        if not item_found and new_order.quantity > 0:
            my_order.append(new_order)

    print(f"Updated order: {my_order}")


@tool
def get_final_price():
    """ Get the final price of the order """
    global my_order
    total_price = sum(item.combined_cost * item.quantity for item in my_order)
    return total_price


# Function to get breakdown of the current order
@tool
def get_breakdown():
    """ function to get the cost breakdown of the order """
    global my_order
    to_return = ""
    total = 0
    for item in my_order:
        to_return += f'{item.item} with {item.add_on}: cost {item.combined_cost}\n'
        total += item.combined_cost
    to_return += f'total order cost is {total}'
    return to_return


tools = [get_menu, update_order, get_final_price, get_add_ons, get_combos, get_breakdown]


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant for a fast food ordering service. Answer all questions to the best of your ability."
            "You are a voice bot, so only return sentences without formatting. ",
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

chain = prompt | llm


MEMORY_HISTORY_STORE = {}


# storing chat history
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in MEMORY_HISTORY_STORE:
        MEMORY_HISTORY_STORE[session_id] = InMemoryChatMessageHistory()
    return MEMORY_HISTORY_STORE[session_id]


agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

CHAIN = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="output",
)


if __name__ == "__main__":
    while True:
        input_text = input("input: ")
        output = CHAIN.invoke({"input": input_text}, config={'configurable': {'session_id': 'foo'}})["output"]
        print(output)
