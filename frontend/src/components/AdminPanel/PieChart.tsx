import { PieChart } from '@mui/x-charts/PieChart';

export default function BasicPie() {
  return (
    <PieChart
      series={[
        {
          data: [
            { id: 0, value: 45, label: 'Other applications/system' },
            { id: 1, value: 35, label: 'This program' },
            { id: 2, value: 20, label: 'Available storage' },
          ],
        },
      ]}
      width={650}
      height={200}
      
    />
  );
}