public class Stack<T> {
    private T[] data;
    private int size;
    
    @SuppressWarnings("unchecked")
    public Stack(int capacity) {
        data = (T[]) new Object[capacity];
        size = 0;
    }

    public void push(T element) {
        if (size >= data.length) {
            throw new StackOverflowError("Стек переполнен");
        }
        data[size] = element;
        size++;
    }

    public T pop() {
        if (size == 0) {
            throw new EmptyStackException("Стек пуст");
        }
        size--;
        T element = data[size];
        data[size] = null;
        return element;
    }

    public T peek() {
        if (size == 0) {
            throw new EmptyStackException("Стек пуст");
        }
        return data[size - 1];
    }

    public boolean isEmpty() {
        return size == 0;
    }
 
    public int getSize() {
        return size;
    }

    public static class EmptyStackException extends RuntimeException {
        public EmptyStackException(String message) {
            super(message);
        }
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>(10);

        stack.push(1);
        stack.push(2);
        stack.push(3);

        System.out.println(stack.peek()); // 3
        System.out.println(stack.getSize()); // 3
        System.out.println(stack.pop()); // 3
        System.out.println(stack.getSize()); // 2
        System.out.println(stack.peek()); // 2
        
        stack.push(4);
        System.out.println(stack.pop()); // 4
        System.out.println(stack.pop()); // 2


        Stack<String> stringStack = new Stack<>(5);
        stringStack.push("Hello");
        stringStack.push("World");
        stringStack.push("Java");
        
        System.out.println(stringStack.pop());
        System.out.println(stringStack.pop());
        System.out.println(stringStack.peek());
        
        System.out.println(stringStack.isEmpty());
        stringStack.pop();
        System.out.println(stringStack.isEmpty());
    }
}