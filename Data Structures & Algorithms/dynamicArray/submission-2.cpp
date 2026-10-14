class DynamicArray {
    int * m_A = nullptr;
    int m_size = 0;
    int m_capacity = 0;
public:

    DynamicArray(int capacity) {
        m_A = new int[capacity]();
        m_capacity = capacity;
    }

    int get(int i) {
        return m_A[i];
    }

    void set(int i, int n) {
        m_A[i] = n;
    }

    void pushback(int n) {
        if (m_size==m_capacity) {
            resize();
        }
        m_A[m_size] = n;
        m_size++;
    }

    int popback() {
        int x = m_A[m_size-1];
        m_size--;
        return x;
    }

    void resize() {
        int * aux = new int[m_capacity*2]();
        for (int i = 0; i < m_size; i++) {
            aux[i] = m_A[i];
        }
        delete[] m_A;
        m_A = aux;
        m_capacity *=2;
    }

    int getSize() {
        return m_size;
    }

    int getCapacity() {
        return m_capacity;
    }
};
