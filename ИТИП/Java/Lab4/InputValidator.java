class CustomInputMismatchException extends Exception {
    public CustomInputMismatchException(String message) {
        super(message);
    }
}

class InputValidator {
    public static int readPositiveInteger(String input) throws CustomInputMismatchException {
        try {
            int value = Integer.parseInt(input);
            if (value <= 0) {
                throw new CustomInputMismatchException(
                    "Введено не положительное число: " + value
                );
            }
            return value;
        } catch (NumberFormatException e) {
            throw new CustomInputMismatchException("Введена не числовая строка: '" + input + "'");
        }
    }
    
    public static void main(String[] args) {
        try {
            System.out.println("Число: " + readPositiveInteger("42"));
            System.out.println("Число: " + readPositiveInteger("ow;ejkfn"));
        } catch (CustomInputMismatchException e) {
            System.out.println("Ошибка: " + e.getMessage());
        }
        try {
            System.out.println("Число: " + readPositiveInteger("-5"));
        } catch (CustomInputMismatchException e) {
            System.out.println("Ошибка: " + e.getMessage());
        }
    }
}