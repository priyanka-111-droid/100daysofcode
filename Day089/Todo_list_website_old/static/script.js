const sortableLists = document.querySelectorAll('.sortable');

let draggedItem = null;

sortableLists.forEach((sortableList) => {
    sortableList.addEventListener('dragstart', (e) => {
        draggedItem = e.target;
        setTimeout(() => {
            e.target.style.display = 'none';
        }, 0);
    });

    sortableList.addEventListener('dragend', (e) => {
        setTimeout(() => {
            e.target.style.display = '';
            draggedItem = null;
        }, 0);
    });

    sortableList.addEventListener('dragover', (e) => {
        e.preventDefault();
        const afterElement = getDragAfterElement(sortableList, e.clientY);
        const currentElement = document.querySelector('.dragging');

        if (afterElement == null) {
            sortableList.appendChild(draggedItem);
        } else {
            sortableList.insertBefore(draggedItem, afterElement);
        }
    });
});

const getDragAfterElement = (container, y) => {
    const draggableElements = [...container.querySelectorAll('li:not(.dragging)')];

    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const offset = y - box.top - box.height / 2;

        if (offset < 0 && offset > closest.offset) {
            return {
                offset: offset,
                element: child,
            };
        } else {
            return closest;
        }
    }, {
        offset: Number.NEGATIVE_INFINITY,
    }).element;
};
