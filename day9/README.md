<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secret Auction Program - Project README</title>
    <!-- Basic styling for readability without external CSS -->
    <style>
        body {
            font-family: 'Inter', sans-serif; /* Using Inter as a preferred font */
            line-height: 1.6;
            margin: 20px;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 900px;
            margin: 20px auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1, h2, h3, h4 {
            color: #2c3e50;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        h1 {
            text-align: center;
            border-bottom: none;
            padding-bottom: 0;
            margin-bottom: 20px;
            display: flex; /* Use flexbox to align emoji and text */
            align-items: center; /* Vertically center items */
            justify-content: center; /* Horizontally center content */
            gap: 10px; /* Space between emoji and text */
        }
        .emoji {
            font-size: 2.5em; /* Make the emoji larger */
            line-height: 1; /* Ensure emoji doesn't add extra line height */
        }
        h2 {
            font-size: 1.8em;
        }
        h3 {
            font-size: 1.4em;
        }
        pre {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9em;
            color: #34495e;
            border: 1px solid #ddd;
        }
        code {
            background-color: #e0e0e0;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9em;
            color: #c0392b;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        ol {
            list-style-type: decimal;
            margin-left: 20px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        /* Removed .logo and .logo pre styles as they are no longer needed */
        .section-separator {
            border: 0;
            height: 1px;
            background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));
            margin: 40px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Replaced ASCII logo with a large emoji next to the title -->
        <h1><span class="emoji">🤫</span> Secret Auction Program</h1>

        <hr class="section-separator">

        <h2>🔒 Overview</h2>
        <p>Welcome to the <strong>Secret Auction Program</strong>! This is a simple, command-line based application that facilitates a blind auction process. Participants can submit their bids secretly, and after all bids are in, the program reveals the highest bidder and the winning amount. This project was developed as a hands-on exercise to practice fundamental Python concepts, including:</p>
        <ul>
            <li><strong>Input and Output:</strong> Gathering user input and displaying results.</li>
            <li><strong>Data Structures:</strong> Using dictionaries to store bidder information.</li>
            <li><strong>Control Flow:</strong> Implementing loops (<code>while</code>) and conditional statements (<code>if/elif/else</code>).</li>
            <li><strong>Functions:</strong> Organizing code into reusable functions for better modularity.</li>
            <li><strong>Clear Screen Functionality:</strong> Enhancing user experience by clearing the console between bids.</li>
        </ul>

        <hr class="section-separator">

        <h2>✨ Features</h2>
        <ul>
            <li><strong>Secret Bidding:</strong> Bids are hidden from other participants.</li>
            <li><strong>Multiple Bidders:</strong> Supports any number of participants.</li>
            <li><strong>Highest Bidder Determination:</strong> Automatically identifies the winner.</li>
            <li><strong>Input Validation:</strong> Ensures that bids entered are valid numbers.</li>
            <li><strong>User-Friendly Interface:</strong> Clears the screen between bids for a clean auction experience.</li>
            <li><strong>Re-run Option:</strong> Allows users to easily start a new auction after one concludes.</li>
        </ul>

        <hr class="section-separator">

        <h2>🚀 How to Run the Program</h2>
        <p>To get this Secret Auction running on your local machine, follow these simple steps:</p>

        <h3>Prerequisites</h3>
        <p>You'll need Python installed on your system. If you don't have it, you can download it from the official Python website: <a href="https://www.python.org/downloads/" target="_blank">python.org</a></p>

        <h3>Installation</h3>
        <ol>
            <li><strong>Clone the repository (or copy the code):</strong>
                <p>If this code is part of a Git repository, you would typically clone it:</p>
                <pre><code>git clone &lt;repository_url&gt;
cd secret-auction-program</code></pre>
                <p><em>(Replace <code>&lt;repository_url&gt;</code> with the actual URL of your repository.)</em></p>
                <p>If you just have the Python file, save the provided code into a file named <code>secret_auction.py</code>.</p>
            </li>
        </ol>

        <h3>Execution</h3>
        <ol>
            <li><strong>Open your terminal or command prompt.</strong></li>
            <li><strong>Navigate to the directory</strong> where you saved <code>secret_auction.py</code>.</li>
            <li><strong>Run the program</strong> using the Python interpreter:
                <pre><code>python secret_auction.py</code></pre>
            </li>
            <li><strong>Follow the on-screen prompts</strong> to enter bidder names and their secret bids.</li>
        </ol>

        <hr class="section-separator">

        <h2>🖥️ Program Output Example</h2>
        <p>Here's a typical interaction and output you would see when running the Secret Auction program:</p>
        <pre><code>
**************************************************
Welcome to Secret Auction App!
**************************************************
What is your name?: Alice
What is your bid? $150
Are there any other bidders? Type 'yes' or 'no'.
yes

**************************************************
You are now bidding in Secret Auction App!
**************************************************
What is your name?: Bob
What is your bid? $180
Are there any other bidders? Type 'yes' or 'no'.
yes

**************************************************
You are now bidding in Secret Auction App!
**************************************************
What is your name?: Charlie
What is your bid? $120
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is Bob with a bid of $180.00
Would you like to run another auction? (yes/no): no
Thank you for using the Secret Auction App! closing app . . . .
goodbye...
        </code></pre>

        <hr class="section-separator">




        <hr class="section-separator">

        <h2>🤝 Contributing</h2>
        <p>This project is a personal learning exercise. However, if you have suggestions for improvements or find any issues, feel free to open an issue or submit a pull request!</p>

        <hr class="section-separator">

        <h2>📄 License</h2>
        <p>This project is open-source and available under the MIT License.</p>
    </div>
</body>
</html>
