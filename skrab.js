const fs = require('fs');
const path = require('path');

// Список разрешенных расширений файлов
const allowedExtensions = ['.js', '.py', '.html', '.css', '.json', '.md'];

// Функция для рекурсивного обхода всех файлов и папок
async function readFilesRecursively(dir, callback) {
    const files = await fs.promises.readdir(dir);
    for (const file of files) {
        const filePath = path.join(dir, file);
        const stat = await fs.promises.stat(filePath);
        if (stat.isDirectory()) {
            // Если это папка, рекурсивно читаем ее
            if (!['node_modules', '__pycache__', '.vscode'].includes(file)) {
                callback(filePath, 'directory');
                await readFilesRecursively(filePath, callback);
            }
        } else {
            // Если это файл, проверяем расширение и вызываем callback
            if (!['skrab.js', 'my_project.txt'].includes(file)) {
                await checkFileExtensionAndProcess(filePath, callback);
            }
        }
    }
}

// Функция для проверки расширения файла и обработки
async function checkFileExtensionAndProcess(filePath, callback) {
    const ext = path.extname(filePath).toLowerCase();
    if (allowedExtensions.includes(ext)) {
        callback(filePath, 'file');
    }
}

// Функция для записи содержимого файла в my_project.txt
async function appendFileContentToFile(filePath, outputPath, type) {
    const relativeFilePath = path.relative(__dirname, filePath);
    if (type === 'directory') {
        const content = `Папка: ${relativeFilePath}\n\n`;
        await fs.promises.appendFile(outputPath, content);
    } else if (type === 'file') {
        const data = await fs.promises.readFile(filePath, 'utf8');
        const content = `Название файла: ${path.basename(filePath)}\nРасположение файла: ./${relativeFilePath}\n\n${data}\n\n`;
        await fs.promises.appendFile(outputPath, content);
        console.log(`Содержимое файла ${filePath} записано в ${outputPath}`);
    }
}

const rootDir = path.join(__dirname, './'); // Путь к корневой папке
const outputFilePath = path.join(__dirname, 'my_project.txt'); // Путь к файлу my_project.txt

// Очищаем или создаем файл my_project.txt
async function main() {
    await fs.promises.writeFile(outputFilePath, 'Структура проекта:\n\n');
    // Начинаем рекурсивный обход файлов и папок
    await readFilesRecursively(rootDir, (filePath, type) => {
        appendFileContentToFile(filePath, outputFilePath, type);
    });
}

main().catch(console.error);
