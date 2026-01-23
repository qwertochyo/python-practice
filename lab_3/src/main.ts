import express, { Request, Response } from 'express';
import bodyParser from 'body-parser';
import { Kafka, Producer } from 'kafkajs';

interface TableMessage {
  table: string;
  columns: string[];
  rows: any[][];
}

function validateMessage(msg: TableMessage): string | null {
  if (!msg.table) return 'Имя таблицы не указано';
  if (!msg.columns || msg.columns.length === 0) return 'Список колонок пуст';
  if (!msg.rows || msg.rows.length === 0) return 'Нет данных в строках';

  for (const row of msg.rows) {
    if (row.length !== msg.columns.length) {
      return 'Количество значений в строке не соответствует количеству колонок';
    }
  }
  return null;
}

class KafkaProducer {
  private producer: Producer;
  private topic: string;

  constructor(brokers: string[], topic: string) {
    const kafka = new Kafka({ brokers });
    this.producer = kafka.producer();
    this.topic = topic;
  }

  async connect() {
    await this.producer.connect();
  }

  async send(msg: TableMessage) {
    await this.producer.send({
      topic: this.topic,
      messages: [{ value: JSON.stringify(msg) }]
    });
  }

  async disconnect() {
    await this.producer.disconnect();
  }
}

async function main() {
  const brokers = ['10.23.28.65:9092'];
  const topic = 'etl-topic';

  const kafkaProducer = new KafkaProducer(brokers, topic);
  await kafkaProducer.connect();

  const app = express();
  app.use(bodyParser.json());

  app.post('/send', async (req: Request, res: Response) => {
    const msg: TableMessage = req.body;

    const error = validateMessage(msg);
    if (error) return res.status(400).send(`Ошибка: ${error}`);

    try {
      await kafkaProducer.send(msg);
      res.status(200).send('Сообщение успешно отправлено в Kafka');
    } catch (err: any) {
      console.error('Ошибка при отправке в Kafka:', err);
      res.status(500).send('Внутренняя ошибка сервера при отправке сообщения');
    }
  });

  app.listen(8080, () => {
    console.log('Продьюсер запущен на http://localhost:8080');
  });

  process.on('SIGINT', async () => {
    console.log('Отключаем Kafka');
    await kafkaProducer.disconnect();
    process.exit(0);
  });
}

main().catch(err => console.error('Ошибка в потоке:', err));
