import { PieChart } from '@mui/x-charts/PieChart';

export default function BasicPie() {
  return (
    <PieChart
      series={[
        {
          data: [
            { id: 0, value: 45, label: 'Studium Regeln' },
            { id: 1, value: 35, label: 'Abschlussarbeit' },
            { id: 2, value: 20, label: 'Praktikum' },
          ],
        },
      ]}
      width={450}
      height={200}
      
    />
  );
}