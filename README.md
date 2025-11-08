# Graph Implementation

โปรแกรมสร้างและแสดงผล Graph โดยใช้ Adjacency List

## คำอธิบาย

โปรแกรมนี้ใช้สร้าง directed graph โดยใช้โครงสร้างข้อมูลแบบ Adjacency List ซึ่งประกอบด้วย:
- **Vertex**: คลาสสำหรับเก็บจุดยอดปลายทางและ pointer ไปยังจุดถัดไป
- **Edge**: คลาสสำหรับเก็บข้อมูลเส้นเชื่อม (จุดเริ่มต้นและจุดปลายทาง)
- **Graph**: คลาสสำหรับจัดการ graph โดยใช้ array ของ linked list

## วิธีใช้งาน

1. รันโปรแกรม:
```bash
python graph.py
```

2. ใส่ข้อมูล:
   - จำนวน vertices (จุดยอด)
   - จำนวน edges (เส้นเชื่อม)
   - คู่ของ edges แต่ละเส้น (start end)

## ตัวอย่าง

```
Enter number of vertices: 5
Enter number of edges: 8
Enter edges (start end):
0 1
0 2
0 3
1 2
1 3
2 3
1 4
3 4
```

## ผลลัพธ์

โปรแกรมจะแสดง adjacency list ของ graph ที่สร้างขึ้น:
```
Graph created is:
( 0 -> 3)	( 0 -> 2)	( 0 -> 1)	
( 1 -> 4)	( 1 -> 3)	( 1 -> 2)	
( 2 -> 3)	
( 3 -> 4)	
```

## โครงสร้างข้อมูล

- ใช้ Adjacency List เพื่อประหยัดพื้นที่หน่วยความจำ
- แต่ละ vertex มี linked list ของ vertices ที่เชื่อมต่อ
- Time Complexity: O(V + E) สำหรับการสร้าง graph
