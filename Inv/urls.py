from django.urls import path, include

from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete,\
                SubcategoriaView, SubcategoriaNew, SubcategoriaEdit, SubcategoriaDelete,\
                MarcaView, MarcaNew, MarcaEdit, marca_inactivar,\
                UnidadMedidaView,UnidadMedidaNew,UnidadMedidaEdit,unidad_medida_inactivar,\
                ProductoView, ProductoNew, ProductoEdit, producto_inactivar

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDelete.as_view(), name='categoria_del'),

    path('subcategorias', SubcategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubcategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubcategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubcategoriaDelete.as_view(), name='subcategoria_del'),
    
    path('marcas', MarcaView.as_view(), name='marca_list'),
    path('marcas/new', MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:id>', marca_inactivar, name='marca_inactivar'),
    
    path('unidad_medida', UnidadMedidaView.as_view(), name='unidad_medida_list'),
    path('unidad_medida/new', UnidadMedidaNew.as_view(), name='unidad_medida_new'),
    path('unidad_medida/edit/<int:pk>', UnidadMedidaEdit.as_view(), name='unidad_medida_edit'),
    path('unidad_medida/inactivar/<int:id>', unidad_medida_inactivar, name='unidad_medida_inactivar'),
    
    path('productos', ProductoView.as_view(), name='producto_list'),
    path('productos/new', ProductoNew.as_view(), name='producto_new'),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('productos/inactivar/<int:id>', producto_inactivar, name='producto_inactivar'),
]