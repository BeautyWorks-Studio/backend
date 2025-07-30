import json

package_json = {
    "name": "backend",
    "version": "1.0.0",
    "description": "",
    "main": "server.js",
    "type": "module",
    "scripts": {
        "start": "node server.js",
        "server": "nodemon server.js"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
        "bcrypt": "^5.1.1",
        "cloudinary": "^2.4.0",
        "cors": "^2.8.5",
        "dotenv": "^16.4.5",
        "express": "^4.19.2",
        "jsonwebtoken": "^9.0.2",
        "mongoose": "^8.5.3",
        "multer": "^1.4.5-lts.1",
        "nodemon": "^3.1.4",
        "razorpay": "^2.9.4",
        "stripe": "^16.8.0",
        "validator": "^13.12.0"
    }
}

if __name__ == "__main__":
    with open("package.json", "w") as f:
        json.dump(package_json, f, indent=2)
        print("package.json has been generated successfully.")
