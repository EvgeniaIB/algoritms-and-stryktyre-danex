class Node:
    """Узел бинарного дерева"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    """Вставка значения в бинарное дерево поиска (BST)"""
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

# --- РЕАЛИЗАЦИЯ ОБХОДОВ ---

def preorder_traversal(root, result=None):
    """Прямой обход (Pre-order): Корень -> Левое -> Правое"""
    if result is None:
        result = []
    if root:
        result.append(root.value)          # 1. Посещаем корень
        preorder_traversal(root.left, result)  # 2. Идем влево
        preorder_traversal(root.right, result) # 3. Идем вправо
    return result

def inorder_traversal(root, result=None):
    """Симметричный обход (In-order): Левое -> Корень -> Правое (выводит по возрастанию)"""
    if result is None:
        result = []
    if root:
        inorder_traversal(root.left, result)   # 1. Идем влево
        result.append(root.value)          # 2. Посещаем корень
        inorder_traversal(root.right, result)  # 3. Идем вправо
    return result

def postorder_traversal(root, result=None):
    """Обратный обход (Post-order): Левое -> Правое -> Корень"""
    if result is None:
        result = []
    if root:
        postorder_traversal(root.left, result)  # 1. Идем влево
        postorder_traversal(root.right, result) # 2. Идем вправо
        result.append(root.value)          # 3. Посещаем корень
    return result

def print_tree(root, level=0, prefix="Корень: "):
    """Красивый вывод дерева в консоль (повернутое на 90 градусов)"""
    if root is not None:
        print_tree(root.right, level + 1, "Право: ")
        print("  " * level + prefix + str(root.value))
        print_tree(root.left, level + 1, "Лево:  ")

if __name__ == "__main__":
    # 1. Создаем дерево
    tree = None
    values = [50, 30, 20, 40, 70, 60, 80]
    
    for val in values:
        tree = insert(tree, val)
        
   
    print("СТРУКТУРА ДЕРЕВА")
    
    # Выводим дерево (корень слева, дети справа)
    print_tree(tree)
    

    print("ОБХОДЫ ДЕРЕВА")
   
    # 2. Прямой обход
    pre = preorder_traversal(tree)
    print(f"Прямой обход (Pre-order):  {pre}")
    
    # 3. Симметричный обход
    ino = inorder_traversal(tree)
    print(f"Симметричный (In-order):   {ino}  <-- Отсортировано по возрастанию")
    
    # 4. Обратный обход
    post = postorder_traversal(tree)
    print(f"Обратный обход (Post-order): {post}")
    