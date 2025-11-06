## Docker Architecture

![สถาปัตยกรรม docker](../sources/images/005/1.png)

### docker client
เครื่องมือสำหรับส่งคำสั่งไปยัง docker host เพื่อควบคุมการทำงานของ docker โดยการใช้คำสั่ง docker cli เช่น docker run, docker build

### docker host 
เครื่องคอมพิวเตอร์หรือเซิร์ฟเวอร์ (Physical หรือ virtual machine) ที่มีการติดตั้ง docker engine เพื่อนใช้รันและจัดการ container

### docker deamon (docker-d)
คือกระบวนการทำงานหลักภายใน docker engine โดยคอยทำงานอยู่เบื้องหลังเพื่อรับคำสั่งจากผู้ใช้งานสำหรับจัดการ images, container, volumns, ติดต่อกับ docker registry, อื่น ๆ

### docker registry (docker hub)
เป็นคลังกลางที่ใช้เก็บ images เพื่อให้นักพัฒนาทั่วโลกสามารถสร้างและแชร์ images ให้กับคนอื่น ๆ ได้