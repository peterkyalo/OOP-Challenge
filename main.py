from pet import Pet

def main():
    print("Creating pet: Max")
    pet = Pet("Max")
    
    pet.eat()
    pet.play()
    pet.sleep()
    
    pet.train("roll over")
    pet.train("play dead")
    
    pet.show_tricks()
    pet.get_status()

if __name__ == "__main__":
    main()