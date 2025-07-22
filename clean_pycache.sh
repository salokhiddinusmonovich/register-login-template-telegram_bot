#!/bin/bash

echo "Deleting all __pycahes__ from project..."

find . -type d -name "__pycache__" -exec rm -rf {} + 

echo "Done!"

