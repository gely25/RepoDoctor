from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Doctor
from applications.core.forms.doctor import DoctorForm
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class DoctorListView(PermissionMixin, ListViewMixin, ListView):
    model = Doctor
    template_name = 'core/doctor/list.html'
    context_object_name = 'doctores'
    permission_required = 'view_doctor'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(nombres__icontains=q1) | Q(apellidos__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:doctor_create')
        return context

class DoctorCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')
    permission_required = 'add_doctor'

    def form_valid(self, form):
        messages.success(self.request, 'Doctor registrado exitosamente.')
        return super().form_valid(form)

class DoctorUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')
    permission_required = 'change_doctor'

    def form_valid(self, form):
        messages.success(self.request, 'Doctor actualizado correctamente.')
        return super().form_valid(form)

class DoctorDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Doctor
    template_name = 'core/delete.html'  # Solo se usa si accedes por URL directa
    success_url = reverse_lazy('core:doctor_list')
    permission_required = 'delete_doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Doctor'
        context['description'] = f"¿Desea eliminar al doctor: {self.object}?"
        context['back_url'] = self.success_url
        return context
