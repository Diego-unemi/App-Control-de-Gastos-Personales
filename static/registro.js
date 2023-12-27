const editor = new DataTable.Editor({
    ajax: '../php/staff.php',
    fields: [
        {
            label: 'First name:',
            name: 'first_name'
        },
        {
            label: 'Last name:',
            name: 'last_name'
        },
        {
            label: 'Position:',
            name: 'position'
        },
        {
            label: 'Office:',
            name: 'office'
        },
        {
            label: 'Extension:',
            name: 'extn'
        },
        {
            label: 'Start date:',
            name: 'start_date',
            type: 'datetime'
        },
        {
            label: 'Salary:',
            name: 'salary'
        }
    ],
    table: '#example'
});
 
const table = new DataTable('#example', {
    ajax: '../php/staff.php',
    columns: [
        {
            data: null,
            render: data => data.first_name + ' ' + data.last_name
        },
        { data: 'position' },
        { data: 'office' },
        { data: 'extn' },
        { data: 'start_date' },
        { data: 'salary', render: DataTable.render.number(null, null, 0, '$') }
    ],
    lengthChange: false,
    select: true
});
 
// Display the buttons
new DataTable.Buttons(table, [
    { extend: 'create', editor },
    { extend: 'edit', editor },
    { extend: 'remove', editor }
]);
 
let insertPoint = table.table().container().querySelectorAll('.col-md-6')[0];
table.buttons().container().appendTo(insertPoint);

