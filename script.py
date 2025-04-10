import os

def create_init_files(root_dir):
    for current_dir, dirnames, _ in os.walk(root_dir):
        # Skip the venv directory
        if 'venv' in current_dir.split(os.sep):
            continue

        init_file = os.path.join(current_dir, '__init__.py')

        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                pass  # Create an empty __init__.py file
            print(f'Created: {init_file}')

# Run the function with the path to your root project directory
if __name__ == '__main__':
    create_init_files('.')  # You can change '.' to your specific root directory path
