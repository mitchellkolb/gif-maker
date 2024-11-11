# test_gifski_pyqt.py
import gifski_pyqt

# Test add_numbers function
result = gifski_pyqt.add_numbers(5, 3)
print(f"add_numbers(5, 3) = {result}")  # Expected output: 8

# Test generate_gif_message function
message = gifski_pyqt.generate_gif_message()
print(f"generate_gif_message() = {message}")  # Expected output: "GIF generated successfully!"


# end tbe fucntion to release rust memory
gifski_pyqt.release()
gifski_pyqt.quit()