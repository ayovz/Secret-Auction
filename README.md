# 🕵️‍♂️ Secret Auction - Python CLI App

This is a simple **command-line based secret auction system** built with Python. Bidders can enter their names and bids one by one, and the screen will be cleared after each entry to maintain secrecy. Once all bids are submitted, the program will reveal the highest bidder and their bid amount.

---

## 🚀 Features

- Secret bidding with screen-clearing after each entry
- Multiple bidders supported
- Displays the highest bidder at the end
- ASCII art header for a fun, thematic interface

---

## 🛠️ How to Run

1. Make sure you have Python installed (version 3+).
2. Copy or clone this script into a `.py` file (e.g., `secret_auction.py`).
3. Open your terminal or command prompt.
4. Run the script:

```bash
python secret_auction.py
```

    💡 Windows users: The screen will clear using cls.
    💡 macOS/Linux users: You may need to change os.system("cls") to os.system("clear").

✍️ Sample Input
```
Enter your name: Alice
Enter your bid: 100
Are there anyone to bid? Yes or No: yes

Enter your name: Bob
Enter your bid: 150
Are there anyone to bid? Yes or No: no
```
🏆 Output
```
Highest bidder: Bob 
Bid: $150
```
📄 License

This project is open-source and free to use for educational or personal purposes.
👨‍💻 Author

    Developed by Ayomal
    Inspired by simple beginner Python projects.
